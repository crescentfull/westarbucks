def get_len_of_str(s):
    # 아래 코드를 작성해주세요
  # 비교값 > 현재값의 저장, 최댓값의 저장
  curr_max = 0
  curr_string = []
  for j in range(len(s)) :
    for i in range(j,len(s)) :
      # 있으면.
      if s[j] in curr_string : #중복값이 잇는지 체크
        if curr_max < len(curr_string) :
          curr_max = len(curr_string)

      #없으면 넣어주기.
      else :
        curr_string.append(s[j]) # 넣어주기
    
    if curr_max < len(curr_string) :
      curr_max = len(curr_string)
  
  return curr_max
    
print(get_len_of_str('abcadeeess'))