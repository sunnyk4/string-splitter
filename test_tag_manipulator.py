from tag_manipulator import TagManipulator

def test_split_empty_string_result_empty_array():
    # arrange
    stringToSplit = ""
    expResult = []
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult

def test_split_comma_empty_string_result_empty_array():
    # arrange
    stringToSplit = ","
    expResult = []
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult

def test_split_one_string_result_array_of_two():
    # arrange
    stringToSplit = "java byte code,python"
    regex = ","
    expResult = ["java byte code","python"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult

def test_strip_string_spaces_before_after():
    # arrange
    stringToSplit = " java "
    regex = ","
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult

def test_strip_string_commas_before_after():
    # arrange
    stringToSplit = ",java"
    regex = ","
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult










