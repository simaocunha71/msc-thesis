import os
import measure_utils as measure_utils
from codecarbon import OfflineEmissionsTracker
from llama_cpp import Llama

class LLAMACPP:
    def __init__(self, label, prompt_file_path, filename, model_name, seed, n_ctx, max_tokens, benchmark_type, save_output_flag, language=None):
        """
        Inicializa a classe LLAMACPP com argumentos fornecidos.
        
        Parameters:
        label (str): Identificador da execução do LLM no ficheiro CSV final.
        prompt_file_path (str): Path do ficheiro de texto que contém o prompt.
        filename (str): Nome do ficheiro CSV final a adicionar o conteúdo (append).
        model_name (str): Path do LLM.
        max_tokens (int): Número máximo de tokens a ser usado pelo LLM na resposta.
        benchmark_type (str): Tipo de benchmark a executar (util para a geração das samples).
        save_output_flag (str): Flag para guardar outputs em ficheiros (true) ou não (false)
        language (str, optional): Linguagem a ser executada no benchmark (argumento opcional).
        """
        self.label = label
        self.prompt_file_path = prompt_file_path
        self.filename = filename
        self.model_name = model_name
        self.max_tokens = max_tokens
        self.benchmark_type = benchmark_type
        self.save_output_flag = save_output_flag
        self.language = language
        self.seed = seed
        self.n_ctx = n_ctx

    def read_prompt(self):
        """
        Lê o prompt do ficheiro especificado e elimina o ficheiro.
        
        Returns:
        str: O conteúdo do prompt.
        """
        with open(self.prompt_file_path, 'r') as prompt_file:
            content = prompt_file.read()

        os.remove(self.prompt_file_path)
        return content
    
    def load_llamacpp(self):
        return Llama(model_path=self.model_name, seed=self.seed, n_ctx=self.n_ctx, verbose=False)


    def execute_llamacpp(self, prompt):
        """
        Executa o objeto LlamaCpp com o prompt fornecido.
        
        Parameters:
        prompt (str): O prompt a ser fornecido ao objeto LlamaCpp.
        
        Returns:
        str: A saída de texto do objeto LlamaCpp.
        """
        llm_object = self.load_llamacpp()
        output = llm_object(prompt=prompt, max_tokens=self.max_tokens, stop=["Q:"], echo=True)["choices"][0]["text"]

        return output

    def run(self):
        """
        Executa o benchmark e mede as emissões de carbono.
        """
        measure_utils.print_measure_information(self.model_name, self.label)
        

        tracker = OfflineEmissionsTracker(country_iso_code="PRT")
        tracker.start()
        prompt = self.read_prompt()
        output = self.execute_llamacpp(prompt)
        tracker.stop()

        def clean_output(output):
            """Remove prompts from n-shot prompting in the output generated"""
            # Find the last occurrence of 'A:\n'
            last_index = output.rfind('A:\n')

            # If 'A:\n' is not found, return early
            if last_index == -1:
                print("No 'A:\n' found in the output.")
                return ""

            # Extract the text following the last 'A:\n'
            cleaned_output = output[last_index + len('A:\n'):]

            return cleaned_output

        
        output = clean_output(output)

        if self.benchmark_type == "humaneval_x":
            measure_utils.generate_samples_humaneval_x(measure_utils.extract_llm_name(self.model_name), output, self.label, self.language)
        elif self.benchmark_type == "mbpp":
            measure_utils.generate_samples_mbpp(measure_utils.extract_llm_name(self.model_name), output, self.label)
        
        if self.save_output_flag == "yes":
            if self.benchmark_type == "humaneval_x":
                measure_utils.save_output_to_file(output, self.label, self.language, "returned_prompts", 
                                                  measure_utils.extract_llm_name(self.model_name), 
                                                  "humaneval_x")

            elif self.benchmark_type == "mbpp":
                measure_utils.save_output_to_file(output, (self.label).replace("/","_"), None, "returned_prompts", 
                                                  measure_utils.extract_llm_name(self.model_name), 
                                                  "mbpp")

        measure_utils.add_measurement_to_csv(self.filename, measure_utils.extract_llm_name(self.model_name), 
                                             self.label, tracker)
        