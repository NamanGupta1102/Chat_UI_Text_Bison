import simpleT5.simplet5.simplet5 as sp
model = sp.SimpleT5()
# model.from_pretrained(model_type="codet5", model_name="Salesforce/codet5-small")
model.load_model("codet5", "https://drive.google.com/drive/folders/15vixFcdc9aOKxEJ-DPZC-_FmB71j65Wq?usp=drive_link")
print(model.predict('eval(input("enter any equation"))'))
print('hi')