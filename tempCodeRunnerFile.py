if "h" in r2.recognize_google(audio):
#     r2 = sr.Recognizer()
#     url = ""
#     with sr.Microphone() as source:
#         print('search your querrry')
#         audio = r2.listen(source)

#         try:
#             get = r2.recognize_google(audio)
#             print(get)
#             wb.get().open_new(url+get)
#         except sr.UnknownValueError:
#             print("eroor")
#         except sr.sr.RequestError as e:
#             print("error".format(e))
