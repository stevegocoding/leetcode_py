# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):


def gen_4(buf):
    i = 0
    while (i < len(buf)):
        step = min(4, len(buf) - i)
        yield buf[i:i+step]
        i += step

gen = None


def read4(buf):
    global gen
    if gen is None:
        return -1
    try:
        temp = next(gen)
        for i, e in enumerate(temp):
            buf[i] = e
    except StopIteration:
        temp = []

    return len(temp)


class Solution:
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def read(self, buf, n):
        r_buf = ['' for i in range(4)]
        r = read4(r_buf)
        count = 0
        while (r != 0 and len(buf) < n):
            for i in range(r):
                buf.append(r_buf[i])
            count += r
            r_buf = ['' for i in range(4)]
            r = read4(r_buf)
        return count


if __name__ == "__main__":
    global gen

    buf = [chr(ord('a') + i) for i in range(10)]
    print buf

    gen = gen_4(buf)

#    r_buf = ['' for i in range(4)]
#    r = read4(r_buf)
#    while (r != 0):
#        print(r_buf)
#        print(r)
#        r_buf = ['' for i in range(4)]
#        r = read4(r_buf)

    d_buf = ["z"]
    n = 1
    l = Solution().read(d_buf, n)

    print d_buf
    print l
