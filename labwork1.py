{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMYcriP5USJj9+gGB1taYa5",
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
        "<a href=\"https://colab.research.google.com/github/khoada2410445-cmd/Python-2026-L1/blob/main/labwork1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Ex1: Calculate the area of a circle"
      ],
      "metadata": {
        "id": "mi6jfm-aX7OB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import math\n",
        "\n",
        "r = float(input(\"Enter circle radius? \"))\n",
        "area = math.pi * r * r\n",
        "print(f\"Circle area = {area}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4OOPB-PfX-O9",
        "outputId": "21dbc5f3-4d14-4e54-c035-470440045c36"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter circle radius? 10\n",
            "Circle area = 314.1592653589793\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Ex2: Convert Celsius (°C) to Fahrenheit (°F)"
      ],
      "metadata": {
        "id": "fiGgNfKNYBAJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "c = float(input(\"Enter the temperature in Celsius? \"))\n",
        "f = (c * 9/5) + 32\n",
        "\n",
        "c_str = int(c) if c.is_integer() else c\n",
        "f_str = int(f) if f.is_integer() else f\n",
        "\n",
        "print(f\"{c_str} (C) = {f_str} (F)\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mC35u9tlYDe4",
        "outputId": "17caa166-91ca-4708-b749-e828e2c44c2b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the temperature in Celsius? 3\n",
            "3 (C) = 37.4 (F)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Ex3: Check if a number is prime"
      ],
      "metadata": {
        "id": "Xx4WgAwPYG7p"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "n = int(input(\"Enter a number? \"))\n",
        "\n",
        "def is_prime(num):\n",
        "    if num < 2:\n",
        "        return False\n",
        "    for i in range(2, int(num**0.5) + 1):\n",
        "        if num % i == 0:\n",
        "            return False\n",
        "    return True\n",
        "\n",
        "if is_prime(n):\n",
        "    print(f\"{n} is a prime number\")\n",
        "else:\n",
        "    print(f\"{n} is a NOT prime number\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-dwX3KKfYLYB",
        "outputId": "81553001-4d6a-4d89-ec82-5a3975ec3002"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number? 6\n",
            "6 is a NOT prime number\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Ex4: Check if a number is a perfect number"
      ],
      "metadata": {
        "id": "6-ZvUAqgYOsy"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "n = int(input(\"Enter a number? \"))\n",
        "\n",
        "def is_perfect(num):\n",
        "    if num < 1:\n",
        "        return False\n",
        "    sum_divisors = sum(i for i in range(1, num) if num % i == 0)\n",
        "    return sum_divisors == num\n",
        "\n",
        "if is_perfect(n):\n",
        "    print(f\"{n} is a perfect number\")\n",
        "else:\n",
        "    print(f\"{n} is a NOT perfect number\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SzPRkPynYSNt",
        "outputId": "951731b8-0d2e-43ea-cc2c-e8266fc63148"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number? 6\n",
            "6 is a perfect number\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Ex5: Find favorite color in a list"
      ],
      "metadata": {
        "id": "LwGzgkziYVyr"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Sample list containing colors with \"Red\" at index 3\n",
        "colors = [\"Blue\", \"Yellow\", \"Black\", \"Red\", \"White\"]\n",
        "\n",
        "user_color = input(\"What is your favorite color? \")\n",
        "\n",
        "if user_color in colors:\n",
        "    index = colors.index(user_color)\n",
        "    print(f\"Your colod is at index {index} in my list\")\n",
        "else:\n",
        "    print(\"Sorry, I could not find your color\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-ouTfX8aYfmt",
        "outputId": "091ddc5f-d1e5-4cf6-cef4-b8a113d630d7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "What is your favorite color? Blue\n",
            "Your colod is at index 0 in my list\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Ex6: Generate sequences using ⁠range()"
      ],
      "metadata": {
        "id": "_S5S4HYtYhtC"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "range1 = list(range(0, 7))\n",
        "range2 = list(range(1, 11, 3))\n",
        "range3 = list(range(5, 0, -1))\n",
        "range4 = list(range(6, -3, -2))\n",
        "\n",
        "print(\"range1:\", range1)\n",
        "print(\"range2:\", range2)\n",
        "print(\"range3:\", range3)\n",
        "print(\"range4:\", range4)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KaFYZjRBYk1A",
        "outputId": "6ba8fabb-8f13-44f9-f79e-f9097adfd806"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "range1: [0, 1, 2, 3, 4, 5, 6]\n",
            "range2: [1, 4, 7, 10]\n",
            "range3: [5, 4, 3, 2, 1]\n",
            "range4: [6, 4, 2, 0, -2]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Ex7: Function to remove dollar sign from a string"
      ],
      "metadata": {
        "id": "JYgVX-pqY5oS"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def remove_dollar_sign(s):\n",
        "    return s.replace(\"$\", \"\")\n",
        "\n",
        "\n",
        "# Test execution\n",
        "text = \"$100.00$\"\n",
        "result = remove_dollar_sign(text)\n",
        "print(\"Result:\", result)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Wu2Q1UdsY8oP",
        "outputId": "32234c5f-3ac0-41f5-aa6c-28b8cd0b0629"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Result: 100.00\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Ex8: Function to extract even numbers from a list"
      ],
      "metadata": {
        "id": "sMcNf596ZICD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def extract_even(l):\n",
        "    return [x for x in l if x % 2 == 0]\n",
        "\n",
        "\n",
        "# Test execution\n",
        "sample_list = [1, 4, 5, -1, 10]\n",
        "result = extract_even(sample_list)\n",
        "print(\"Result:\", result)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7zv3RU2yZMsk",
        "outputId": "79a236d4-f14c-4c4a-adbc-c70fdd502c99"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Result: [4, 10]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Ex9: Function to calculate factorial"
      ],
      "metadata": {
        "id": "5pxQ7BRWa6Ua"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def factorial(n):\n",
        "    if n == 0 or n == 1:\n",
        "        return 1\n",
        "    result = 1\n",
        "    for i in range(2, n + 1):\n",
        "        result *= i\n",
        "    return result\n",
        "\n",
        "\n",
        "# Test execution\n",
        "number = 5\n",
        "result = factorial(number)\n",
        "print(f\"Factorial of {number} = {result}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Nfy5ochGbD0y",
        "outputId": "aac01820-ceb0-4ade-bfb9-2d88ffca1eb9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Factorial of 5 = 120\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Ex10: Function to get all divisors of a number"
      ],
      "metadata": {
        "id": "i6f9rVhLbHqf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def get_divisors(n):\n",
        "    return [i for i in range(1, n + 1) if n % i == 0]\n",
        "\n",
        "\n",
        "# Test execution\n",
        "number = 12\n",
        "result = get_divisors(number)\n",
        "print(f\"Divisors of {number} = {result}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pPSrH9C7bM-c",
        "outputId": "ba40c421-4bbd-46ad-ba5f-96b4aae44f9c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Divisors of 12 = [1, 2, 3, 4, 6, 12]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Ex11: Compute distance between two points"
      ],
      "metadata": {
        "id": "R_wRsdqBcpla"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import math\n",
        "\n",
        "x1 = float(input(\"Enter x1: \"))\n",
        "y1 = float(input(\"Enter y1: \"))\n",
        "x2 = float(input(\"Enter x2: \"))\n",
        "y2 = float(input(\"Enter y2: \"))\n",
        "\n",
        "distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)\n",
        "print(f\"Distance = {distance}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "F4OX_A3MctQn",
        "outputId": "6108cd09-fd05-4971-ec54-9ffc5947acc6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter x1: 1\n",
            "Enter y1: 2\n",
            "Enter x2: 3\n",
            "Enter y2: 4\n",
            "Distance = 2.8284271247461903\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Ex12: Print pattern of size m x n"
      ],
      "metadata": {
        "id": "sFaRrhTscv8I"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def print_pattern(m, n):\n",
        "    for i in range(m):\n",
        "        if i == 0 or i == m - 1:\n",
        "            print(\"* \" * n)\n",
        "        else:\n",
        "            print(\"* \" + \"  \" * (n - 2) + \"*\")\n",
        "\n",
        "\n",
        "# Test execution\n",
        "m = int(input(\"Enter number of rows (m): \"))\n",
        "n = int(input(\"Enter number of columns (n): \"))\n",
        "print_pattern(m, n)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PcrsUryLcytZ",
        "outputId": "c0322ee4-6c8f-47e2-aff5-73a4a94fb63c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter number of rows (m): 4\n",
            "Enter number of columns (n): 5\n",
            "* * * * * \n",
            "*       *\n",
            "*       *\n",
            "* * * * * \n"
          ]
        }
      ]
    }
  ]
}