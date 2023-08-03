from markup import remove_html_markup


def test_abc():
    assert remove_html_markup("abc") == "abc"


def test_b_abc_b():
    assert remove_html_markup("<b>abc</b>") == "abc"


def test_quoted_abc():
    assert remove_html_markup('"abc"') == '"abc"'
