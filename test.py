import pytest


class TestDemo:
    def test_1(self):
        assert 1 == 1

    def test_2(self):
        print(1)
        assert 1 == 21


if __name__ == '__main__':
    pytest.main(['-sq', 'test.py'])
