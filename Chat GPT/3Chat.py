import openai
openai.api_key = "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" 
Start = True
def ask_question(conversation):
    response = openai.Completion.create(
        engine="text-davinci-002", # specify which GPT model to use
        prompt=conversation,
        max_tokens=3072, # maximum length of the generated response
        n=4, # how many responses to generate
        )
    print('-------------------------------------START_ANSWER-----------------------------------------\n')
    print(response.choices[0].text.strip())
    print('\n--------------------------------------END_ANSWER------------------------------------------')
	
while Start == True:    
    conversation = input("Enter Any Q To Ask Chat GPT : ") 
    if conversation == "Q":
      Start = False
    else:  
      ask_question(conversation)   