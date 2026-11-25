言語処理100本ノック
===================

[言語処理100本ノック 2025](https://nlp100.github.io/2025/ja/) の解答をまとめるリポジトリです。

## 章一覧

- [1. 準備運動](1.準備運動/README.md)（00〜09）

## 構成

各章を「番号.章タイトル」のフォルダに分けています。

- `knockNN.py`：解答コード（1問1ファイル。Google Colabのセルにそのまま貼って動く）
- `output/outputNN.txt`：実行結果
- `README.md`：各問の解説メモ

## 実行方法

Python 3.12 と [uv](https://docs.astral.sh/uv/) を使います。リポジトリ直下で実行します。

```
uv run python 1.準備運動/knock00.py > 1.準備運動/output/output00.txt
```

Windowsでは、リダイレクトしたときに日本語がShift_JIS（cp932）で保存されることがあります。
PowerShell 7.4以降を使い、先に次を実行しておくとUTF-8で保存されます。

```powershell
$env:PYTHONUTF8 = "1"
```
