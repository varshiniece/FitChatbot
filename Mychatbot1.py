import openai
###.  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
def askGPT(text):
    openai.api_key = "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"
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = text,
        temperature = 0.6,
        max_tokens = 150
    )
    return print(response.choices[0].text)
def main():
    while True:
        print('BOT: Heyya... Ask me a question. I am your fitness coach. ')
        myQn = input()
        askGPT(myQn)
        print('\n')

main()
