from ocr_reader import extract_multiplier


def test_multiplier():
    assert extract_multiplier("2.50x") == 2.50
    assert extract_multiplier("10.25x") == 10.25
    assert extract_multiplier("1,75x") == 1.75
    assert extract_multiplier("Tidak ada angka") is None

    print("Semua pengujian berhasil!")


if __name__ == "__main__":
    test_multiplier()
