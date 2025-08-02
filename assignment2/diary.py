import traceback

try:
    with open ('diary.txt', 'a') as file:
        response = ""
        initial = True
        while (response != "done for now"):
            if initial:
                response = input("What happened today? ")
                file.write(response + '\n')
                initial = False
            else: 
                response = input("What else? ")
                file.write(response + '\n')
        file.write("done for now")

except Exception as e:
   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = list()
   for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
   print(f"Exception type: {type(e).__name__}")
   message = str(e)
   if message:
      print(f"Exception message: {message}")
   print(f"Stack trace: {stack_trace}")