import openai

# OpenAI configuration

openai.api_type = "azure"

openai.api_base = "https://coe-openai-instance.openai.azure.com/"

openai.api_version = "2023-03-15-preview"

openai.api_key = "d079f278137e44a8812fc39fe85449eb"

def askLLM(system_context, user_context):
    dict_response = {}
    messages = [{"role": "system", "content": system_context}, {"role": "user", "content": user_context}]
    engine = "coe-gpt-4"
    response_gtp_4 = openai.ChatCompletion.create(engine=engine, messages=messages, temperature=0)
    dict_response['result'] = response_gtp_4['choices'][0]['message']['content']
    llm_response = dict_response['result']
    return llm_response

def read_groovy_file(file_path):
    try:
        with open(file_path, 'r') as file:
            groovy_contents = file.read()
            return groovy_contents
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
file_path = 'sample.groovy'
groovy_string = read_groovy_file(file_path)

system_context = '''I will provide you a Jenkinsfile. I want you to tell me everything about the file. It should be very detailed
                    and without errror.'''

res = askLLM(system_context, groovy_string)
print("Description of the script provided.")
print("---------------------------------------------------------------------------------")
print("/n"+res)
print("---------------------------------------------------------------------------------")


system_context = '''You will be provided a Jenkinsfile. You need to convert the file into a Json where each key represent variables,
                    tasks, steps, stages, agent and their respective values.'''
res = askLLM(system_context, groovy_string)
print("Json Structure to check if the LLM is able to identify every syntax")
print("---------------------------------------------------------------------------------")
print(res)
print("---------------------------------------------------------------------------------")

system_context = '''You will be provided a Jenkinsfile. Convert it to YAML file for azure pipeline. Be very careful. Comment out anything
                    you want to inform the user and where you think human intervention is necessary. Only return the YAML file and nothing else.'''
res = askLLM(system_context, groovy_string)
print("The YAML file for your azure pipeline")
print("---------------------------------------------------------------------------------")
print(res)
print("---------------------------------------------------------------------------------")

