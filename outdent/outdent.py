""" Custom outdentation, with a codec """

import sys
import codecs


def outdent(lines):
    counted = []
    for l in lines:
        if l:
            for i, c in enumerate(l):
                if not c.isspace():
                    break

            counted.append((i, l))

    max_indented = max(counted, key=lambda x: x[0])

    out = []
    for c, l in counted:
        out.append(' '*(max_indented[0]-c) + l.strip())

    return '\n'.join(out)


if __name__ == "__main__":
    content = sys.stdin.read()
    lines = content.splitlines()
    print(outdent(lines))
    sys.exit()


encode = codecs.utf_8_encode


def decode(input, errors="strict"):
    return codecs.utf_8_decode(input, errors, True)


class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.utf_8_encode(input, self.errors)[0]


class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    _buffer_decode = codecs.utf_8_decode

    def decode(self, input, final):
        if input:
            input = outdent(input.decode().splitlines()).encode()
        return super().decode(input, final)


class StreamWriter(codecs.StreamWriter):
    encode = codecs.utf_8_encode


class StreamReader(codecs.StreamReader):
    decode = codecs.utf_8_decode


outdent_encoding = codecs.CodecInfo(
    name="outdent",
    encode=encode,
    decode=decode,
    incrementalencoder=IncrementalEncoder,
    incrementaldecoder=IncrementalDecoder,
    streamreader=StreamReader,
    streamwriter=StreamWriter,
)

codecs.register({"outdent": outdent_encoding}.get)
