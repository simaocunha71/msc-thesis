from transformers import pipeline

#code = ".count() <mask> 0;" # Buggy line 7: notice we mask the operator
code = """public boolean containsStudent(String id) {
        return students.stream().filter(x -> x.getId().equals(id)).count() <mask> 0;
    }"""
    
# Simple way to ask CodeBERT to fill in the mask
fill_mask = pipeline('fill-mask', model="microsoft/codebert-base-mlm")
outputs = fill_mask(code)

# Check the generations
print("\nGenerations:")
for o in outputs:
    print(o)
