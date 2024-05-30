from src.nlu_utils import classify_text

def test_classify_text():
    text = "This is a test sentence."
    candidate_labels = ["greeting", "statement"]
    classification = classify_text(text, candidate_labels)
    assert classification is not None
    assert isinstance(classification, dict)
 
