import sys
from subprocess import run, PIPE
from os import listdir, remove
from os.path import join, splitext, isfile
from datetime import datetime
from time import sleep

def update_dependency_field(file_path, jobid):
    """
    Update JobID dependency statement in provided file and write to a new file with .sh extension
    """
    base, ext = splitext(file_path)
    temp_file_path = f"{base}_temp{ext}"

    with open(file_path, 'r') as tmp_file:
        linhas = tmp_file.readlines()

    new_lines = [linha.replace("$DEPS", jobid) for linha in linhas]

    with open(temp_file_path, 'w') as tmp_file2:
        tmp_file2.writelines(new_lines)
    
    return temp_file_path

"""
Este script tem como objetivo ser executado aquando da realizacao dos testes IB.3
"""

scripts_folder = '/home/ldap/simaocunha71/scripts_test'

def main():
    submited_jobs = []
    slurm_scripts = scripts_folder
    temp_files = []

    # Filtrar apenas os scripts .sh
    scripts = [f for f in listdir(slurm_scripts) if f.endswith('.sh')]
    
    # Especifique o nome do primeiro script a ser executado
    first_script_name = "starling_humanevalx_python_0shot.sh"
    
    # Verifique se o script especificado está na lista e o remova
    if first_script_name in scripts:
        scripts.remove(first_script_name)
    else:
        print(f"Erro: {first_script_name} não encontrado em {slurm_scripts}.")
        sys.exit(1)

    # Submeter o primeiro script sem dependência
    print(f"First script: {first_script_name}")
    first_script_path = join(slurm_scripts, first_script_name)
    submit_cmd = f"sbatch {first_script_path}"

    proc = run(submit_cmd, shell=True, stdout=PIPE)
    output = proc.stdout.decode('ascii')
    print(f"Output do sbatch: {output}")

    if len(output.split()) >= 4:
        previous_jobid = output.split()[3]
    else:
        print(f"Erro ao submeter o script {first_script_name}: {output}")
        sys.exit(1)

    print(f"Script {first_script_name} running with job id {previous_jobid}")
    submited_jobs.append(int(previous_jobid))
    print(f"Submited job {previous_jobid}")
    sleep(1)

    # Submeter os demais scripts com dependência
    for script in scripts:
        script_path = join(slurm_scripts, script)
        temp_file_path = update_dependency_field(script_path, previous_jobid)  # Atualiza a dependência
        
        # Armazena o caminho do arquivo temporário para remoção posterior
        temp_files.append(temp_file_path)
        
        submit_cmd = f"sbatch {temp_file_path}"
        proc = run(submit_cmd, shell=True, stdout=PIPE)
        output = proc.stdout.decode('ascii')

        if len(output.split()) >= 4:
            previous_jobid = output.split()[3]
        else:
            print(f"Erro ao submeter o script {script}: {output}")
            sys.exit(1)

        print(f"Script {script} running with job id {previous_jobid}")
        submited_jobs.append(int(previous_jobid))
        print(f"Submited job {previous_jobid}")
        sleep(1)

    # Remover todos os arquivos temporários após a execução
    for temp_file in temp_files:
        if isfile(temp_file):
            remove(temp_file)

if __name__ == '__main__':
    main()
