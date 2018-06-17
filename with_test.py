class TestWtih():
    def __enter__(self):
        print('enter')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print('normal')
        else:
            print('has error')


# 优雅做法
with TestWtih():
    print('test is running')
    raise NameError()

