import simpleT5.simplet5.simplet5 as sp
model = sp.SimpleT5()
# model.from_pretrained(model_type="codet5", model_name="Salesforce/codet5-small")
model.load_model("codet5", "Code_T5_Small_Working")
# print(model.predict('eval(input("enter any equation"))'))
# print('hi')
# instruct = "You are a Code Security expert specifically for python. For every python code given to you, you will give exactly 3 reccomendations on how to make the code more secure."
instruct = "\n Give a recommendation for making this code more secure: Give me the most important 3 points to secure this code. Answer in three sentences only, and be specific"
def predict(bad_code):
    return model.predict(bad_code+instruct)
# print(predict("eval(input('enter some equation'))"))