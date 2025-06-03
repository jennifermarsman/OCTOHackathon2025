from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)

client = AzureOpenAI(  
  base_url = "https://octo-hackathon-eastus2.openai.azure.com/openai/v1/",  
  azure_ad_token_provider=token_provider,
  api_version="preview"
)

response = client.responses.create(
    input = "Write a 3-paragraph biography of Jennifer Marsman.",
    model = "o3", # replace with model deployment name
    stream = True
)

for event in response:
    if event.type == 'response.output_text.delta':
    #if event.type == 'response.reasoning_summary_text.delta':
        print(event.delta, end='')

