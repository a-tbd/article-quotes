from analize_text_test import parse_article


def test_parse_article():
    """A sanity check to make sure we don't lose text when parsing into sentences."""
    # Note this is not just any file. I had to hand-remove funny double quotes and replace them with regular ones.
    test_fname = 'test_data/small.txt'
    data = parse_article(test_fname)
    with open(test_fname, 'r') as f:
        original = f.read()

    # Check that we split into sentences correctly (not losing information)
    recreate_text = ''.join([sentence['text'] for sentence in data['sentences'].values()])

    # remove newlines and spaces for comparison.
    core_text = original.replace('\n', '').replace(' ', '')
    recreate_text = recreate_text.replace('\n', '').replace(' ', '')
    assert recreate_text == core_text
