# LZ77 Tools

## 使用示例

```bash
python LZ77.py -r example.txt -M Q
```

以上命令会对 `example.txt` 文件中存放的LZ77压缩的数据进行解压，并尝试转换为二维码

具体使用方式可以通过执行 `python LZ77.py -h` 查看
```bash
+-----------------------------------------------------+
+                    CTF Misc                         +
+                   LZ77 Tools                        +
+                    By Dalock                        +
+-----------------------------------------------------+
usage: LZ77.py [-h] -r READ [-M {Q,S,QS}] [-o OUTPUT]

LZ77 decompression tool

options:
  -h, --help           show this help message and exit
  -r, --read READ      Read the file and get the IDAT data
  -M {Q,S,QS}          Mode: Q for QR code, S for string, QS for both
  -o, --output OUTPUT  Output the QRCode to a file
```

## 原理
### IDAT（图像数据块）

IDAT块包含实际的图像数据，即压缩算法的输出流。数据流中可包含多个连续顺序的图像数据块。

 - 储存图像像素数据
 - 在数据流中可包含多个连续顺序的图像数据块
 - 采用 LZ77 算法的派生算法进行压缩
 - 可以用 zlib 解压缩

**IDAT块只有当上一个块充满时，才会继续下一个新块**

IDAT块的结构为：
<p align="center">
    <img src="1.png" alt="IDAT块结构">
</p>
块数据部分存储的就是通过LZ77 算法的派生算法进行压缩的，当在这部分藏了信息需要提取时，可以通过zlib解压缩