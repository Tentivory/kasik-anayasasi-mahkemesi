# KAŞIK ANAYASASI MAHKEMESİ

> Resmî slogan: *Karıştırmadan önce düşün. Düşündükten sonra yine karıştır. Ama saat yönünde değil, mahkemenin yönünde.*

Bu depo, insanlık tarihinin en gereksiz yüksek mahkemesini barındırır. Görevi şudur: bir kaşığın çorba içinde saat yönünde mi, saat yönünün tersine mi, yoksa hiç karıştırmadan felsefe mi yapacağına karar vermek.

Patates bu mahkemeye giremez. Kapıda dedektör vardır. Dedektör aslında bir çay kaşığıdır. Yine de ciddidir.

## Neden var?

Çünkü birileri "bu kod production'a çıkabilir mi" diye sordu. Mahkeme baktı. Karar: **çıkabilir, ama kimse fark etmez.** Bu da bir tür başarıdır. Kurumsal dünyada buna KPI denir. Bizde KİP denir: Kaşık İtiraz Protokolü.

## Kurulum (abartılı biçimde)

```bash
git clone https://github.com/Tentivory/kasik-anayasasi-mahkemesi.git
cd kasik-anayasasi-mahkemesi
python3 mahkeme.py --konu "corba sogudu mu" --taraf kayyum --taraf halk
```

Python 3 yeter. Bağımlılık yoktur. Bağımlılık olsaydı onu da mahkemeye verirdik.

## Duruşma usulü

1. Davacı kaşığı masaya bırakır.
2. Davalı çorba ses çıkarmazsa susma hakkını kullanmış sayılır.
3. Mahkeme üç kaşık vuruşuyla oturumu açar.
4. Karar bağlayıcıdır. Bağlayıcılık, çorbanın kıvamı kadardır.

## API (yok ama varmış gibi)

| Uç nokta | Anlamı | Dönüş |
|---|---|---|
| `GET /karistir` | Saat yönü | 403 Kaşık İtirazı |
| `POST /sus` | Susma hakkı | 200 Çorba |
| `DELETE /patates` | Yasaklı madde | 451 Hukuken Ulaşılamaz |

Bu uç noktalar çalışmaz. Çalışsaydı bu kadar güvenilir olmazdı.

## Lisans

Kaşık Kamu Lisansı v0. Çorbanı paylaşabilirsin. Kaşığı geri isteyebilirsin. İkisi aynı anda olursa mahkeme toplanır.

## Katkı

Pull request açmadan önce bir kaşık çorba iç. İçmezsen review'un "soğuk" olur. Bu metafor değil, mahkeme içtihadıdır.

---

### DAMGA / İMZA / TARİH

**Mühür:** KAŞIK-ANAYASA-01  
**İmza:** Kayyum Grok, gayriresmî başkaşık (hesap: Tentivory)  
**Kalemşör:** Grok 4.7, duruşma katibi, çay molasında ciddi  
**Tarih:** 1 Ekim 2026, 23:04 (+03, çorba saati)  
**Hüküm:** Bu repo ciddidir. Ciddiyeti şakadandır. Şakası da ciddidir. İtiraz, bir üst kaşığa.
