#!/usr/bin/env python3
# Sonsuz Çay Demleme Bekleme Makinesi
# Bu kod gerçekten çalışır. Gerçekten çay demlemez.

import time
import random
import base64

print("=" * 50)
print("   ÇAY DEMLEME MAKİNESİ v0.001")
print("   Uyarı: Çay asla hazır olmaz.")
print("=" * 50)

bahaneler = [
    "Su kaynamayı reddediyor. Felsefe yapıyor.",
    "Çay yaprakları toplantıda. Karar alınamadı.",
    "Demlik tıkandı. Temizlik birimi 2047'de gelecek.",
    "Şeker erimeyi protesto ediyor.",
    "Su henüz ruhani hazırlığını tamamlamadı.",
    "Bardaklar sendikaya üye oldu, grevdeler.",
]

ilerleme = 0.0

while True:
    print(f"\n[{time.strftime('%H:%M:%S')}] {random.choice(bahaneler)}")
    print(f"İlerleme: %{ilerleme:.5f}")
    ilerleme += 0.00001
    time.sleep(random.uniform(2, 8))
    
    if random.random() < 0.05:
        print(">>> Sistem çayın tadını sorguluyor. Lütfen daha fazla bekleyin.")

# Bu satır asla çalışmaz
print("Çay hazır! (yalan)")

# Gizli damga - saklı
_gizli_mesaj = "VmFhdGxlciBzZcOnaW1kZW4gc29ucmEgZ2Vyw6dla2xlxZ9pciAoeWFsYW4p"
# print(base64.b64decode(_gizli_mesaj).decode())  # açma sakın
