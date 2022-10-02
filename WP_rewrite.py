import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def rewrite(sentence):
    tokenizer = AutoTokenizer.from_pretrained("Vamsi")  
    model = AutoModelForSeq2SeqLM.from_pretrained("Vamsi")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    text =  "paraphrase: " + sentence + " </s>"

    encoding = tokenizer.encode_plus(text,padding=True, return_tensors="pt")

    input_ids, attention_masks = encoding["input_ids"].to(device), encoding["attention_mask"].to(device)

    outputs = model.generate(
        input_ids=input_ids, attention_mask=attention_masks,
        max_length=256,
        do_sample=True,
        top_k=200,
        top_p=0.95,
        early_stopping=True,
        num_return_sequences=5
    )

    LinesWithNum = []

    for count, output in enumerate(outputs):
        line = tokenizer.decode(output, skip_special_tokens=True,clean_up_tokenization_spaces=True)
        LinesWithNum.append(str(count+1)+") "+line)

        #print(LinesWithNum[count])
    return LinesWithNum


print(rewrite("This is something which i cannot understand at all"))
