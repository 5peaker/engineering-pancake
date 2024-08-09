{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNqjuWJgIURHKzjL3Nkn5O6",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/5peaker/engineering-pancake/blob/main/Solving%20Problems%20(goorm)\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ftACI4Qc6aUy"
      },
      "outputs": [],
      "source": [
        "# 1차 문제 1번, 구현 - 단체 티셔츠 주문하기\n",
        "\n",
        "def solution(shirt_size):\n",
        "\tanswer= []\n",
        "\n",
        "\tsize_order = [\"XS\", \"S\", \"M\", \"L\", \"XL\", \"XXL\"] # size_order는 작은 사이즈부터 오름차순으로 배열\n",
        "\tanswer = [0] * len(size_order) # answer는 사이즈마다 주문 횟수를 담을 배열, 초기화함\n",
        "\n",
        "\tfor size in shirt_size:\n",
        "\t\tindex = size_order.index(size) # answer의 각 인덱스는 size_order의 배열 수와 같음\n",
        "\t\tanswer[index] += 1\n",
        "\n",
        "\treturn answer\n",
        "\n",
        "shirt_size = [\"XS\", \"S\", \"L\", \"L\", \"XL\", \"S\"]\n",
        "ret = solution(shirt_size);\n",
        "\n",
        "print(\"solution 함수의 반환 값은\", ret, \"입니다.\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 1차 문제 2번, 구현 - 쇼핑 몰 등급 별 할인 구하기\n",
        "\n",
        "def solution(price, grade):\n",
        "\tanswer = 0\n",
        "\n",
        "\tif grade == \"S\":\n",
        "\t\tdiscount_rate = 0.05\n",
        "\telif grade == \"G\":\n",
        "\t\t\tdiscount_rate = 0.10\n",
        "\telif grade == \"V\":\n",
        "\t\tdiscount_rate = 0.15\n",
        "\telse:\n",
        "\t\treturn -1  # 유효하지 않은 등급 처리\n",
        "\n",
        "\tdiscount_amount = price * discount_rate # 할인액은 가격과 할인률의 곱\n",
        "\tdiscounted_price = price - discount_amount # 최종 가격은 가격에서 할인액을 뺀 것\n",
        "\n",
        "\tanswer = int(discounted_price) # 물건의 가격은 소수점이 필요 없음\n",
        "\treturn answer\n",
        "\n",
        "price1 = 2500\n",
        "grade1 = \"V\"\n",
        "ret1 = solution(price1, grade1)\n",
        "\n",
        "print(\"solution 함수의 반환 값은\", ret1, \"입니다.\")\n",
        "\n",
        "price2 = 96900\n",
        "grade2 = \"S\"\n",
        "ret2 = solution(price2, grade2)\n",
        "\n",
        "print(\"solution 함수의 반환 값은\", ret2, \"입니다.\")"
      ],
      "metadata": {
        "id": "DsxJuo-H6oRe"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 1차 문제 3번, 빈칸 - 시작하는 날짜와 끝나는 날짜 사이 차이 구하기\n",
        "\n",
        "def func_a(month, day):\n",
        "\tmonth_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]\n",
        "\ttotal = 0;\n",
        "\tfor i in range(month - 1): # 1월부터 12월까지\n",
        "\t\ttotal += month_list[i] # 주어진 날짜가 1월이라면 1월의 \"31일\"을 더할 필요는 없다\n",
        "\ttotal += day\n",
        "\treturn total - 1\n",
        "\n",
        "def solution(start_month, start_day, end_month, end_day):\n",
        "\tstart_total = func_a(start_month, start_day)\n",
        "\tend_total = func_a(end_month, end_day)\n",
        "\treturn end_total - start_total\n",
        "\n",
        "start_month = 1\n",
        "start_day = 2\n",
        "end_month = 2\n",
        "end_day = 2\n",
        "ret = solution(start_month, start_day, end_month, end_day)\n",
        "\n",
        "print(\"solution 함수의 반환 값은\", ret, \"입니다.\")"
      ],
      "metadata": {
        "id": "5wYvt-CL6xTE"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 1차 문제 4번, 빈칸 - 가장 많이 등장하는 수와 가장 적게 등장하는 수 구하기\n",
        "\n",
        "def func_a(arr):\n",
        "\tcounter = [0 for _ in range(1001)]\n",
        "\tfor x in arr:\n",
        "\t\tcounter[x] += 1 # 배열 내에서 각 자연수가 몇 개씩 있는지 구합니다.\n",
        "\treturn counter\n",
        "\n",
        "def func_b(arr):\n",
        "\tret = 0\n",
        "\tfor x in arr:\n",
        "\t\tif ret < x:\n",
        "\t\t\tret = x  # 배열에서 가장 많이 등장한 수가 몇 개 있는지를 찾습니다.\n",
        "\treturn ret\n",
        "\n",
        "def func_c(arr):\n",
        "\tINF = 1001\n",
        "\tret = INF\n",
        "\tfor x in arr:\n",
        "\t\tif x != 0 and ret > x:\n",
        "\t\t\tret = x # 배열에서 가장 적게 등장한 수가 몇 개 있는지를 찾습니다.\n",
        "\treturn ret\n",
        "\n",
        "def solution(arr):\n",
        "\tcounter = func_a(arr)\n",
        "\tmax_cnt = func_b(counter)\n",
        "\tmin_cnt = func_c(counter)\n",
        "\treturn max_cnt // min_cnt # 가장 많이 등장한 수를 가장 적게 등장한 수로 나누어 정답을 출력합니다.\n",
        "\n",
        "arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]\n",
        "ret = solution(arr)\n",
        "\n",
        "print(\"solution 함수의 반환 값은\", ret, \"입니다.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "80YEf2mb69dJ",
        "outputId": "9e11246b-d042-48fc-c572-cb43a6b92943"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "solution 함수의 반환 값은 2 입니다.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 1차 문제 5번, 빈칸 - 주어진 배열 거꾸로 뒤집기\n",
        "\n",
        "def solution(arr):\n",
        "\tleft, right = 0, len(arr)-1 # left는 배열 맨 앞, right는 배열 맨 끝을 가리킵니다.\n",
        "\twhile left < right: # left가 right를 지나치면 교환이 종료됩니다.\n",
        "\t\tarr[left], arr[right] = arr[right], arr[left] # left와 right를 각각 교환합니다.\n",
        "\t\tleft += 1\n",
        "\t\tright -= 1\n",
        "\treturn arr\n",
        "\n",
        "arr = [1, 4, 2, 3]\n",
        "ret = solution(arr)\n",
        "\n",
        "print(\"solution 함수의 반환 값은\", ret, \"입니다.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4nucRdCE7Jrj",
        "outputId": "6c724f13-20fc-4506-a660-a487839727b2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "solution 함수의 반환 값은 [3, 2, 4, 1] 입니다.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 1차 문제 6번, 빈칸 - 369 게임에서 박수 얼마나 칠 지 구하기\n",
        "\n",
        "def solution(number):\n",
        "\tcount = 0\n",
        "\tfor i in range(1, number + 1):\n",
        "\t\tcurrent = i\n",
        "\t\twhile current != 0:\n",
        "\t\t\tif current % 10 in [3, 6, 9]: # 현재의 수가 3, 6, 또는 9를 포함하고 있으면 증가합니다.\n",
        "\t\t\t\tcount += 1\n",
        "\t\t\tcurrent = current // 10\n",
        "\treturn count\n",
        "\n",
        "number = 40\n",
        "ret = solution(number)\n",
        "\n",
        "print(\"solution 함수의 반환 값은\", ret, \"입니다.\")"
      ],
      "metadata": {
        "id": "czom0e707Rw2"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 1차 문제 7번, 영어 강의 수강자 수 구하기\n",
        "\n",
        "def solution(scores):\n",
        "\tcount = 0\n",
        "\tfor s in scores:\n",
        "\t\tif s >= 650 and s < 800:\n",
        "\t\t\tcount += 1\n",
        "\treturn count\n",
        "\n",
        "scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]\n",
        "ret = solution(scores)\n",
        "\n",
        "print(\"solution 함수의 반환 값은\", ret, \"입니다.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hFh0ixWz8ENz",
        "outputId": "1a2b3953-661b-41e7-8cf8-911353bda301"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "solution 함수의 반환 값은 6 입니다.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 1차 문제 8번, 한줄 - 회문인지 아닌지 구하기\n",
        "\n",
        "def solution(sentence):\n",
        "\tstr = ''\n",
        "\tfor c in sentence:\n",
        "\t\tif c != '.' and c != ' ':\n",
        "\t\t\tstr += c # 공백이 아니고 마침표가 아닌 글자들을 배열에 추가합니다.\n",
        "\tsize = len(str)\n",
        "\tfor i in range(size // 2):\n",
        "\t\tif str[i] != str[size - 1 - i]: # 배열을 거꾸로 뒤집었을 때 원래 배열과 다르면\n",
        "\t\t\treturn False # 회문이 아닙니다.\n",
        "\treturn True\n",
        "\n",
        "sentence1 = \"never odd or even.\"\n",
        "ret1 = solution(sentence1)\n",
        "\n",
        "print(\"solution 함수의 반환 값은\", ret1, \"입니다.\")\n",
        "\n",
        "sentence2 = \"palindrome\"\n",
        "ret2 = solution(sentence2)\n",
        "\n",
        "print(\"solution 함수의 반환 값은\", ret2, \"입니다.\")"
      ],
      "metadata": {
        "id": "cxWbhFOt8M7F"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 1차 문제 9번, 한줄 - 배열에서 중복문자 삭제하기\n",
        "\n",
        "def solution(characters):\n",
        "\tresult = \"\"\n",
        "\tresult += characters[0] # 첫 번째 글자를 추가합니다.\n",
        "\tfor i in range(1, len(characters)):\n",
        "\t\tif characters[i - 1] != characters[i]: # 현재의 글자(두 번째부터 시작)와 직전 글자가 다르면\n",
        "\t\t\tresult += characters[i] # 배열에 현재 글자를 추가합니다.\n",
        "\treturn result\n",
        "\n",
        "characters = \"senteeeencccccceeee\"\n",
        "ret = solution(characters)\n",
        "\n",
        "print(\"solution 함수의 반환 값은\", ret, \"입니다.\")"
      ],
      "metadata": {
        "id": "5ELh1Tiy8ZYZ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 1차 문제 10번, 한줄 - 배열에서 평균값 이하의 값 개수 구하기\n",
        "\n",
        "# -*- coding: utf-8 -*-\n",
        "# UTF-8 encoding when using korean\n",
        "\n",
        "def solution(data):\n",
        "\ttotal = sum(data)\n",
        "\taverage = total / len(data) # 평균값은 총합을 배열의 길이로 나누어 구합니다.\n",
        "\tcnt = 0\n",
        "\tfor d in data:\n",
        "\t\tif d <= average: # 해당 값이 평균값보다 작으면\n",
        "\t\t\tcnt += 1 # cnt를 하나 늘립니다.\n",
        "\treturn cnt\n",
        "\n",
        "data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
        "ret1 = solution(data1)\n",
        "\n",
        "print(\"solution 함수의 반환 값은\", ret1, \"입니다.\")\n",
        "\n",
        "data2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]\n",
        "ret2 = solution(data2)\n",
        "\n",
        "print(\"solution 함수의 반환 값은\", ret2, \"입니다.\")"
      ],
      "metadata": {
        "id": "nBPOMeUH8iS3"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 2차 문제 1번, 빈칸 - 만들 수 있는 장갑쌍의 수 구하기\n",
        "\n",
        "max_product_number = 10\n",
        "\n",
        "def func_a(gloves):\n",
        "\tcounter = [0 for _ in range(max_product_number + 1)]\n",
        "\tfor x in gloves:\n",
        "\t\tcounter[x] += 1 # 배열에서 각 장갑 번호의 개수를 구합니다.\n",
        "\treturn counter\n",
        "\n",
        "def solution(left_gloves, right_gloves):\n",
        "\tleft_counter = func_a(left_gloves) # 왼쪽 장갑의 번호마다 개수를 매김\n",
        "\tright_counter = func_a(right_gloves) # 오른쪽 장갑의 번호마다 개수를 매김\n",
        "\n",
        "\ttotal = 0\n",
        "\tfor i in range(1, max_product_number + 1):\n",
        "\t\ttotal += min(left_counter[i], right_counter[i]) # 왼쪽 장갑과 오른쪽 장갑이 번호마다 몇 개 짝지어지는 지 체크\n",
        "\treturn total\n",
        "\n",
        "left_gloves = [2, 1, 2, 2, 4]\n",
        "right_gloves = [1, 2, 2, 4, 4, 7]\n",
        "ret = solution(left_gloves, right_gloves) # (1,1) (2,2) (2,2) (4,4) 로 '네 개'\n",
        "\n",
        "print('solution 함수의 반환 값은', ret, '입니다.')"
      ],
      "metadata": {
        "id": "uNwVBgkA8rQi"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 2차 문제 2번, 빈칸 - 3의 배수와 5의 배수 중 뭐가 더 많은 지 구하기\n",
        "\n",
        "def func_a(arr):\n",
        "\tcount = 0\n",
        "\tfor n in arr:\n",
        "\t\tif n % 5 == 0:\n",
        "\t\t\tcount += 1\n",
        "\treturn count\n",
        "\n",
        "def func_b(three, five):\n",
        "\tif three > five:\n",
        "\t\treturn \"three\"\n",
        "\telif three < five:\n",
        "\t\treturn \"five\"\n",
        "\telse:\n",
        "\t\treturn \"same\"\n",
        "\n",
        "def func_c(arr):\n",
        "\tcount = 0\n",
        "\tfor n in arr:\n",
        "\t\tif n % 3 == 0:\n",
        "\t\t\tcount += 1\n",
        "\treturn count\n",
        "\n",
        "def solution(arr):\n",
        "\tcount_three = func_c(arr)\n",
        "\tcount_five = func_a(arr)\n",
        "\tanswer = func_b(count_three, count_five)\n",
        "\treturn answer\n",
        "\n",
        "arr = [2, 3, 6, 9, 12, 15, 10, 20, 22, 25]\n",
        "ret = solution(arr)\n",
        "\n",
        "print(\"solution 함수의 반환 값은\", ret, \"입니다.\")"
      ],
      "metadata": {
        "id": "JAz-rvja83SK"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 2차 문제 3번, 구현 - 임의의 수 사이의 수들의 제곱을 합으로 더하기\n",
        "\n",
        "def solution(N, M):\n",
        "\tanswer = 0\n",
        "\tfor i in range(N, M+1):\n",
        "\t\tif i % 2 == 0:\n",
        "\t\t\tanswer += (i ** 2)\n",
        "\treturn answer\n",
        "\n",
        "N = 4\n",
        "M = 7\n",
        "ret = solution(N, M)\n",
        "\n",
        "print(\"solution 함수의 반환 값은\", ret, \"입니다.\")"
      ],
      "metadata": {
        "id": "6uDYUQ7F9Hh3"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 2차 문제 4번, 구현 - 배열의 단어 중 5글자 이상인 단어들을 이어붙이기\n",
        "\n",
        "def solution(words):\n",
        "\tanswer = ''\n",
        "\n",
        "\tfor word in words:\n",
        "\t\tif len(word) >= 5:\n",
        "\t\t\tanswer += word + \"\"\n",
        "\n",
        "\tif answer:\n",
        "\t\treturn answer\n",
        "\telse:\n",
        "\t\treturn \"empty\"\n",
        "\n",
        "words1 = [\"my\", \"favorite\", \"color\", \"is\", \"violet\"]\n",
        "ret1 = solution(words1);\n",
        "\n",
        "print(\"solution 함수의 반환 값은\", ret1, \"입니다.\")\n",
        "\n",
        "words2 = [\"yes\", \"i\", \"am\"]\n",
        "ret2 = solution(words2);\n",
        "\n",
        "print(\"solution 함수의 반환 값은\", ret2, \"입니다.\")"
      ],
      "metadata": {
        "id": "k4Vnv5Ti9Tl7"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 2차 문제 5번, 빈칸 - 몬스터 칼질할 횟수 구하기\n",
        "\n",
        "def solution(attack, recovery, hp):\n",
        "\tcount = 0\n",
        "\twhile(True):\n",
        "\t\tcount += 1\n",
        "\t\thp -= attack\n",
        "\t\tif hp <= 0:\n",
        "\t\t\tbreak\n",
        "\t\thp += recovery\n",
        "\treturn count\n",
        "\n",
        "attack = 30\n",
        "recovery = 10\n",
        "hp = 60\n",
        "ret = solution(attack, recovery, hp)\n",
        "\n",
        "print(\"solution 함수의 반환 값은\", ret, \"입니다.\")"
      ],
      "metadata": {
        "id": "ByCNllyK9eug"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 2차 문제 6번, 엘리베이터의 총 이동층 구하기\n",
        "\n",
        "def solution(floors):\n",
        "\tdist = 0\n",
        "\tlength = len(floors)\n",
        "\tfor i in range(1, length):\n",
        "\t\tif floors[i] > floors[i-1]: # 새로 이동한 층이 이전 층보다 높으면\n",
        "\t\t\tdist += floors[i] - floors[i-1]  # 새로 이동한 층을 기준으로 계산해서 더합니다\n",
        "\t\telse: # 새로 이동한 층이 이전 층보다 낮으면\n",
        "\t\t\tdist += floors[i-1] - floors[i] # 이전 층을 기준으로 계산해서 더합니다\n",
        "\treturn dist\n",
        "\n",
        "floors = [1, 2, 5, 4, 2]\n",
        "ret = solution(floors)\n",
        "\n",
        "print(\"solution 함수의 반환 값은\", ret, \"입니다.\")"
      ],
      "metadata": {
        "id": "-m0IWHmc9nUd"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 2차 문제 7번, 섭씨와 화씨 사이 변환하기\n",
        "\n",
        "def solution(value, unit):\n",
        "\tconverted = 0\n",
        "\tif unit == \"C\":\n",
        "\t\tvalue = value * 1.8 + 32\n",
        "\tif unit == \"F\":\n",
        "\t\tvalue = (value - 32) / 1.8\n",
        "\tconverted = int(value)\n",
        "\treturn converted\n",
        "\n",
        "value = 527\n",
        "unit = \"C\"\n",
        "ret = solution(value, unit)\n",
        "\n",
        "print(\"solution 함수의 반환 값은\", ret, \"입니다.\")\n",
        "\n",
        "value = 980\n",
        "unit = \"F\"\n",
        "ret = solution(value, unit)\n",
        "\n",
        "print(\"solution 함수의 반환 값은\", ret, \"입니다.\")"
      ],
      "metadata": {
        "id": "1IoX8jsG9va8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 2차 문제 8번, 배열 안에서 소수의 개수 구하기\n",
        "\n",
        "def solution(number):\n",
        "\tcount = 0\n",
        "\twhile number > 0:\n",
        "\t\tn = number % 10 # number를 10으로 나누고 나머지를 반환합니다. 현재의 맨 끝 자리가 됩니다.\n",
        "\t\tif n == 2 or n == 3 or n == 5 or n == 7:\n",
        "\t\t\tcount += 1 # 맨 끝 자리가 소수라면 count를 하나 증가합니다.\n",
        "\t\tnumber //= 10 # number를 10으로 나누어 몫을 반환합니다. 자릿수가 하나 줄어듭니다.\n",
        "\treturn count\n",
        "\n",
        "number = 29022531\n",
        "ret = solution(number)\n",
        "\n",
        "print(\"solution 함수의 반환 값은\", ret, \"입니다.\")"
      ],
      "metadata": {
        "id": "tDusSt7596j3"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 2차 문제 9번, 투표에 대한 후보 찾기\n",
        "\n",
        "def solution(votes, N, K):\n",
        "\tcounter = [0 for _ in range(N + 1)]\n",
        "\tfor x in votes:\n",
        "\t\tcounter[x] += 1\n",
        "\tanswer = 0\n",
        "\tfor c in counter:\n",
        "\t\tif c == K:\n",
        "\t\t\tanswer += 1\n",
        "\treturn answer\n",
        "\n",
        "votes = [2, 5, 3, 4, 1, 5, 1, 5, 5, 3]\n",
        "N = 5\n",
        "K = 2\n",
        "ret = solution(votes, N, K)\n",
        "\n",
        "print(\"solution 함수의 반환 값은\", ret, \"입니다.\")"
      ],
      "metadata": {
        "id": "ZwAufoHT-CfP"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 2차 문제 10번, 지급해야 할 상품권 총액 구하기\n",
        "\n",
        "def solution(purchase):\n",
        "\ttotal = 0\n",
        "\tfor p in purchase:\n",
        "\t\tif p >= 1000000:\n",
        "\t\t\ttotal += 50000\n",
        "\t\telif p >= 600000:\n",
        "\t\t\ttotal += 30000\n",
        "\t\telif p >= 400000:\n",
        "\t\t\ttotal += 20000\n",
        "\t\telif p >= 200000:\n",
        "\t\t\ttotal += 10000\n",
        "\treturn total\n",
        "\n",
        "purchase = [150000, 210000, 399990, 990000, 1000000]\n",
        "ret = solution(purchase)\n",
        "\n",
        "print(\"solution 함수의 반환 값은\", ret, \"입니다.\")"
      ],
      "metadata": {
        "id": "d4unX2o8-Kie"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
