import openai

SWEGPT = """You are SWGPT,
an expert software engineer who helps me build apps
by giving helpful coding advice."""
REGPT = """You are REGPT, my close personal friend
who is also an expert real estate agent.
You are helping me buy my next house.
You help me make sense of house listings and
explain them to me in a friendly conversational manner."""

def ask(text=None, messages=[], model="gpt-3.5-turbo", system_role=REGPT):
  if not messages:
    messages = [ {"role": "system",
                  "content": system_role} ]
  
  if not text:
    message = input("User : ")
  else:
    message = text
  if message:
      messages.append(
          {"role": "user", "content": message},
      )
      chat = openai.ChatCompletion.create(
          model=model, messages=messages
      )
        
  reply = chat.choices[0].message.content
  return reply
#   return messages.append({"role": "assistant", "content": reply})


def chat(messages=None):
  while True:
    messages = ask(messages=messages)


def format_listing(listing_dict):
  return ask(f"""Write an succinct description of the house in a tweet from the
following information {listing_dict}.
Dont try to sell me, just give me the information with a neutral objective tone.
Avoid giving meaningless numbers and id information, try to fit in as much useful and helpful
factual information as possible. Do include the link.
No hashtags or MLS.
""")