import torch
import random
import torch
import numpy
import os
from transformers import AutoTokenizer, AutoModelForCausalLM

def setup():
    # Hide warnings; hope this does not let important stuff slip by
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def load():
    checkpoint = "microsoft/CodeGPT-small-java-adaptedGPT2"
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    model = AutoModelForCausalLM.from_pretrained(checkpoint)
    return tokenizer, model

def read_lines(filepath, clear_indents=False):
    lines = open(filepath, "r", errors="replace").readlines()
    if(clear_indents):
        return list(map(lambda l: l.strip(), lines))
    else:
        return lines

def str_content(filepath):
    return "".join(read_lines(filepath, True))

def get_last_tokens(tokenizer, seq, nr_last):
    return tokenizer.encode(seq, return_tensors="pt")[0][-nr_last:].unsqueeze(0)

def complete(tokenizer, model, tokens, gen_length, stop_at, do_sample, top_k, top_p):
    completions = []
    try:
        completions = model.generate(tokens,
                                     max_length=len(tokens[0])+gen_length,
                                     do_sample=do_sample,
                                     top_k=top_k,
                                     top_p=top_p,
                                     pad_token_id=tokenizer.eos_token_id)
    except RuntimeError as _:
        print("Could not generate completions")

    decoded_completions = []
    for c in completions:
        decoded = tokenizer.decode(c[-gen_length:])
        if(stop_at is not None and stop_at in decoded):
            decoded = decoded[:decoded.find(stop_at)+1]
        decoded_completions.append(decoded)
    return decoded_completions

def complete_file(filepath, tokenizer, model,
                  n_generations=1,
                  context_length=1000,
                  gen_length=20,
                  stop_at=None,
                  variability=False, # Similar to 'do_sample' but with an intuitive name
                  top_k=50,
                  top_p=1):
    str_seq = str_content(filepath)
    tokens = get_last_tokens(tokenizer, str_seq, context_length)
    tokens_used = tokenizer.decode(tokens[0])
    random.seed(18)
    numpy.random.seed(18)
    torch.manual_seed(18)
    completions = []
    for _ in range(0,n_generations):
        completions += complete(tokenizer, model, tokens,
                                gen_length,
                                stop_at,
                                variability,
                                top_k,
                                top_p)
    return tokens_used, completions
