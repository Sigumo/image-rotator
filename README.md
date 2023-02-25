# Image Rotator

## How to use

* Install requirements
  * `pip install -r requirements.txt`
  * Use virtual environment (i.e. Conda or Virtualenv)
* Place images in `./images` directory
* Run `./main.py` in terminal
  * You may need to allow execution with `chmod +x ./main.py`

## Supported options

* `-c` `--clean` - clean result directory beforehand (defaults to `false`)
* `-i` `--input` - input directory (defaults to `./images`)
* `-o` `--output` - results directory (defaults to `./result_images`)
* `-s` `--step` - rotation step (defaults to `1`)
* `--crop-size` - size to crop image into rectangle (defaults to `640`)
* `--without-mirror` - don't add mirrored versions (defaults to `false`)

## Example

`python main.py -c -i ./images -o ./result_images -s 90`