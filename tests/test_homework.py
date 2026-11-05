"""Regression tests for the homework description shapes Nuvola may return."""

from custom_components.nuvola.homework import homework_description


def test_string_description():
    assert homework_description({"descrizione": "  Leggere pag. 4  "}) == "Leggere pag. 4"


def test_live_field_list_of_strings():
    assert homework_description({
        "descrizioneCompito": ["Leggere pag. 4", "Fare esercizi 2 e 3"],
    }) == "Leggere pag. 4\nFare esercizi 2 e 3"


def test_live_field_list_of_dicts():
    assert homework_description({
        "descrizioneCompito": [
            {"testo": "Leggere pag. 4"},
            {"descrizione": "Fare esercizi 2 e 3"},
        ],
    }) == "Leggere pag. 4\nFare esercizi 2 e 3"


def test_empty_or_missing_returns_none():
    assert homework_description({}) is None
    assert homework_description({"descrizione": "", "descrizioneCompito": []}) is None
    assert homework_description({"descrizioneCompito": None}) is None


def test_invalid_unknown_shapes_do_not_become_python_repr():
    assert homework_description({
        "descrizioneCompito": [{"id": 42, "nonTesto": "privato"}],
    }) is None
    assert homework_description({"descrizioneCompito": 100}) is None


def test_fallback_and_nested_structures():
    assert homework_description({
        "descrizione": " ",
        "descrizioneCompito": [
            {"contenuto": ["Primo punto", {"testo": "Secondo punto"}]},
        ],
    }) == "Primo punto\nSecondo punto"


def test_prefer_existing_description():
    assert homework_description({
        "descrizione": "Testo originale",
        "descrizioneCompito": ["Altra versione"],
    }) == "Testo originale"
