# CRC32碰撞
工具支持对于1-5字节的字符串进行CRC32碰撞，更高位当然也可以，但问题在于效率比较低，这里是对所有的ascii可打印字符进行爆破

如果知道内容只是为数字，可以调整爆破的字符集，提高效率

## 使用示例

```bash
python crc32.py -f example.zip -b 4
```

以上命令会对 `example.zip` 文件进行CRC32碰撞，目标中所有文件大小都为4字节

具体使用方式可以通过执行 `python crc32.py -h` 查看
```bash
+-----------------------------------------------------+
+                    CTF Misc                         +
+           压缩包CRC32碰撞获取文件内容               +
+                    By Dalock                        +
+-----------------------------------------------------+
usage: crc32.py [-h] -r ZIP_PATH -b {1,2,3,4,5}

Process zip file and find CRC32 matches.

options:
  -h, --help            show this help message and exit
  -r, --zip_path ZIP_PATH
                        Path to the zip file
  -b, --char_count {1,2,3,4,5}
                        Number of characters to brute force
```

## 原理
CRC（冗余校验码），CRC32表示会产生一个32bit的校验值

在产生CRC32时，**源数据块的每一位**都参与了运算，因此即使数据块中只有一位发生改变也会得到不同的CRC32值，利用这个原理我们可以直接爆破出加密文件的内容

**由于CPU能力，CRC碰撞只能用于压缩文件较小的情况**

适用于压缩包中有多个小文件的情况，可以碰撞出文件的内容

<p align="center">
    <img src="1.png" alt="CRC32碰撞示例">
</p>

