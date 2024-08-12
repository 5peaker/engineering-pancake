
# [DIY] 점심 뭐 먹을지 구하는 함수

import csv
import random

def lunchOption(file_path):
    lunch_options = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # print(row)  # Debug print to check the row contents
            lunch_options.append({
                'name': row['name'].strip(),
                'time': float(row['time'].strip()),
                'price': float(row['price'].strip()),
                'category': row['category'].strip(),
            })
    return lunch_options

def recommendLunch(lunch_options, max_time, max_price, preferred_category=None):
  yourOptions = [
      option for option in lunch_options
      if option['time'] <= max_time and option['price'] <= max_price
  ]

  if preferred_category:
    yourOptions = [
        option for option in yourOptions
        if option['category'] == preferred_category
    ]

  if not yourOptions:
    return "이번에는 적절한 메뉴를 추천하기 어렵습니다."

  return random.choice(yourOptions)

def get_preferred_cat():
  return input("지금 떠오른 메뉴 입력: ").strip()

def main():
  file_path = 'lunch_options.csv'
  lunch_options = lunchOption(file_path)

  max_time = 10
  max_price = 10.0
  preferred_category = get_preferred_cat()

  recommendation = recommendLunch(lunch_options, max_time, max_price, preferred_category)
  if isinstance(recommendation, dict):
    print("오늘은 이걸 먹을까요?: ", recommendation['name'])
  else:
    print("오늘은 이걸 먹을까요?: ", recommendation)

if __name__ == "__main__":
  main()