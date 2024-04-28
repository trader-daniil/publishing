from dotenv import load_dotenv
from google.cloud import dialogflow
import os
import json

from google.oauth2 import service_account

load_dotenv()

#GOOGLE_APPLICATION_CREDENTIALS=C:\Users\Даниил\AppData\Roaming\gcloud\application_default_credentials.json


LANGUAGE_CODE = 'ru'


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    """Create an intent of the given intent type."""

    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )

    print("Intent created: {}".format(response))


def list_intents(project_id):
    from google.cloud import dialogflow

    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)

    intents = intents_client.list_intents(request={"parent": parent})

    for intent in intents:
        print("=" * 20)
        print("Intent name: {}".format(intent.name))
        print("Intent display_name: {}".format(intent.display_name))
        print("Action: {}\n".format(intent.action))
        print("Root followup intent: {}".format(intent.root_followup_intent_name))
        print("Parent followup intent: {}\n".format(intent.parent_followup_intent_name))

        print("Input contexts:")
        for input_context_name in intent.input_context_names:
            print("\tName: {}".format(input_context_name))

        print("Output contexts:")
        for output_context in intent.output_contexts:
            print("\tName: {}".format(output_context.name))



def main():
    project_id = os.getenv('PROJECT_ID')
    tg_user_id = os.getenv('TG_USER_ID')
    with open('questions.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    for indent, indent_data in data.items():
        create_intent(
            project_id=project_id,
            display_name=indent,
            training_phrases_parts=indent_data['questions'],
            message_texts=[indent_data['answer']],
        )    
    print(list_intents(project_id=project_id))
 

if __name__ == '__main__':
    main()