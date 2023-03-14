text = "X-DSPAM-Confidence:    0.8475"
Start = text.find('0')
End = len(text)
print(float(text[Start: End]))
