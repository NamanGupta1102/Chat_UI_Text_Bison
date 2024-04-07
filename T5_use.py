import simpleT5.simplet5.simplet5 as sp
model = sp.SimpleT5()

model.load_model("t5", "SKaup/t5_small_optimized_secured")

instruct_secure = "\n Give a recommendation for making this code more secure: Give me the most important 3 points to secure this code. Answer in three sentences only, and be specific"
instruct_optimize = "\n Give a recommendation for making this code more optimize: Give me the most important 3 points to optimize this code. Answer in three sentences only, and be specific"

def T5_predict_secure(bad_code):
    return model.predict(bad_code+instruct_secure)[0]

def T5_predict_optimize(bad_code):
    return model.predict( bad_code + instruct_optimize )[0]

