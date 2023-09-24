import sys
import argparse
import openai

INSERT = "[insert]"

def request(model, prompt, instructions, suffix=None,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0):
    if model == "text-davinci-003":
        if suffix is None:
            response = openai.Completion.create(
                model=model, prompt=prompt,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty)
        else:
            response = openai.Completion.create(
                model=model, prompt=prompt, suffix=suffix,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty)
    elif model == "code-davinci-edit-001":
        response = openai.Edit.create(
            model=model,
            input=prompt,
            instruction=instructions,
            temperature=0,
            top_p=top_p)
    return response

def str_content(filename):
    with open(filename) as file:
        return file.read()

def set_api_key():
    api_key_filename = "openai.api_key"
    openai.api_key = str_content(api_key_filename).strip()

def setup_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt_file")
    parser.add_argument("-c", "--complete", action="store_true")
    parser.add_argument("-e", "--edit", type=str, help="use GPT in Edit mode; arg is a string with instructions")
    parser.add_argument("-i", "--insert", action="store_true")
    return parser.parse_args()

def setup_model(args):
    if args.complete or args.insert:
        model = "text-davinci-003"
        instructions = ""
    else:
        model = "code-davinci-edit-001"
        instructions = args.edit
    return model, instructions

def setup():
  set_api_key()

def mk_request(prompt_file, mode, instructions=""):
  prompt = str_content(prompt_file)
  suffix = None

  if mode == "complete" or mode == "insert":
    model = "text-davinci-003"
    instructions = ""
    if mode == "insert":
      prompt, suffix = prompt.split(INSERT)
  elif mode == "edit":
    model = "code-davinci-edit-001"
    instructions = instructions
  else:
    print(mode + "is not supported")
    return

  openai_response = request(model, prompt, instructions, suffix=suffix)
  aux_response = {}
  aux_response["this_mode"] = mode
  aux_response["this_prompt"] = prompt
  aux_response["this_suffix"] = suffix
  return openai_response, aux_response

def show_response(response):
  openai_response, aux_response = response[0], response[1]
  if aux_response["this_mode"] == "insert":
    print(aux_response["this_prompt"], end='')

  print(openai_response["choices"][0]["text"])

  if aux_response["this_mode"] == "insert":
    print(aux_response["this_suffix"], end='')
