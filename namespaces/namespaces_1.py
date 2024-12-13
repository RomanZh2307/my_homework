def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function() # ничего не возвращает

inner_function() # выдает ошибку, что имя функции не определено

test_function() # программа работатет