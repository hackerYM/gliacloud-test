urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
]

def solution(urls):  # O(N * logN) / N = len(urls)

    file_count = {}

    for url in urls:
        file_name = url.split("/")[-1]
        file_count[file_name] = file_count.get(file_name, 0) + 1

    file_count_list = [(k, v) for k, v in file_count.items()]
    file_count_list = sorted(file_count_list, key=lambda x: -x[1])

    print_len = len(file_count_list) if len(file_count_list) < 3 else 3

    for file_name, count in file_count_list[:print_len]:
        print(file_name, count)


if __name__ == '__main__':
    solution(urls)
