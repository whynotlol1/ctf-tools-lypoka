import os
import numpy as np
import pyboof as pb


class QR_Extractor:
    def __init__(self):
        self.detector = pb.FactoryFiducial(np.uint8).qrcode()

    def extract(self, img_path):
        if not os.path.isfile(img_path):
            return None
        image = pb.load_single_band(img_path, np.uint8)
        self.detector.detect(image)
        qr_codes = []
        for qr in self.detector.detections:
            qr_codes.append({
                'text': qr.message,
                'points': qr.bounds.convert_tuple()
            })
        return qr_codes


def read_qr():
    for _ in range(1):  # Specify the algorithm for selecting filenames before using!
        try:
            filename = f"QR_codes/.png"  # Specify the algorithm for selecting filenames before using!
            f = open(filename, "r")
            f.close()
            qr_scanner = QR_Extractor()
            output = qr_scanner.extract(filename)
            print(f"{filename}: {output[0]['text']}")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    read_qr()
