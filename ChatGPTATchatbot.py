import openai
import json
import requests
openai.api_key = ""
url = "https://queue-times.com/parks/1/queue_times.json"
response = requests.get(url)
def compress_array(array):
  """Compresses an array by removing unnecessary spaces and using as few characters as possible.

  Args:
    array: The array to compress.

  Returns:
    The compressed array.
  """

  # Remove all consecutive spaces.
  array = ''.join(array).replace('  ', ' ')

  # Remove all leading and trailing spaces.
  array = array.strip()

  # Return the compressed array.
  return array

if response.status_code == 200:
  rides = json.loads(response.content)
messages = [{"role": "system", "content": "You are a helpful assistant for Alton Towers. You ONLY provide information relating to alton towers (e.g queue times, closest rides, information about rides). You must not provide any information at all that does not relate directly to the park. EVER. This data shows current status of rides: (use it to answer questions to do with rides)" + str(rides)}]
def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

while True:
    user_input = input("You: ")
    print(CustomChatGPT(user_input))
