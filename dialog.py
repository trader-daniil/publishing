from google.cloud import dialogflow


def detect_intent_texts(project_id, session_id, texts, language_code, empty_response=False):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(
        project_id,
        session_id,
    )
    text_input = dialogflow.TextInput(
        text=texts[0],
        language_code=language_code,
    )
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(
        request={
            "session": session,
            "query_input": query_input,
        }
    )
    if response.query_result.intent.is_fallback and empty_response:
        return None
    return response.query_result.fulfillment_text
    
