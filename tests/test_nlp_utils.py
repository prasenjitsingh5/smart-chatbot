from src.nlp_utils import preprocess_text

def test_preprocess_text():
    text = "This is a test sentence."
    processed_text = preprocess_text(text)
    assert processed_text is not None
    assert isinstance(processed_text, str)
 
