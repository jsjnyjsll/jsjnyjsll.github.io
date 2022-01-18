import os
import librosa
import soundfile as sf


def normlize(indir, outdir, sampling_rate=16000):
    """ Normlize wav
    Input Data: 
        LJSpeech目录下的 metadata.csv 和wav
    Output Data:
        *.wav 归一化的波形
    """
    cnt = 0
    os.makedirs(outdir, exist_ok=True)
    for fname in os.listdir(indir):
        if fname[-4:] != ".wav":
            continue

        wav_path = os.path.join(indir, fname)
        out_path = os.path.join(outdir, fname)
        
        if os.path.exists(wav_path):
            wav, _ = librosa.load(wav_path, sampling_rate)
            wav = wav / max(abs(wav))
            sf.write(
                out_path,
                wav,
                sampling_rate,
                subtype='PCM_16'
            )
            cnt+=1
    print("Normlize %d files" % cnt)


if __name__ == "__main__":
    # wav_dir_list=[
    #     r".\amt_abx_20210929\fs-to-taco\fs2_baseline",
    #     r".\amt_abx_20210929\fs-to-taco\tacotron2_baseline"
    # ]
    wav_dir_list = [
        "recording",
    ]
    in_root = '.\\'
    out_root = '.\\norm\\'
    for dirname in wav_dir_list:
        normlize(
            in_root + dirname, 
            out_root + dirname,
        )

