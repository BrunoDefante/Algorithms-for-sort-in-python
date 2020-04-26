from os import system

system('pip install pandas')
system('pip install openpyxl')


import time
import random
import pandas as pd


class sort_algorithms(object):
    def bubble_sort(self, lista):
        elementos = len(lista)-1
        ordenado = False

        while not ordenado:
            ordenado = True
            for i in range(elementos):
                if lista[i] > lista[i+1]:
                    lista[i], lista[i+1] = lista[i+1], lista[i]
                    ordenado = False

        return lista

    def merge_sort(self, lista):
        # lista = lista
        if len(lista) > 1:
            mid = len(lista) // 2
            left = lista[:mid]
            right = lista[mid:]

            self.merge_sort(left)
            self.merge_sort(right)

            i = 0
            j = 0

            k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    lista[k] = left[i]
                    i += 1
                else:
                    lista[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                lista[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                lista[k] = right[j]
                j += 1
                k += 1
        return lista

    def insertion_sort(self, arr):

        for i in range(1, len(arr)):

            key = arr[i]

            j = i-1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr

    def partition(self, arr, low, high):
        i = (low-1)
        pivot = arr[high]

        for j in range(low, high):

            if arr[j] <= pivot:
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)

    def quickSort(self, arr, low, high):
        if low < high:

            pi = self.partition(arr, low, high)

            self.quickSort(arr, low, pi-1)
            self.quickSort(arr, pi+1, high)
        return arr

    def counting_sort(self, array1, max_val):
        m = max_val + 1
        count = [0] * m

        for a in array1:
            # count occurences
            count[a] += 1
        i = 0
        for a in range(m):
            for c in range(count[a]):
                array1[i] = a
                i += 1
        return array1


class randomNumbers():
    def create_random_numbers(self, size):
        lista = []
        lista = list(range(size))
        random.shuffle(lista)
        return lista


def handlerTime(sortType, listRandomRange):
    sort = sort_algorithms()
    rand = randomNumbers()
    inicio = time.time()
    if(sortType == 'bubble_sort' and listRandomRange <= 10000):
        for i in range(1):
            sort.bubble_sort(rand.create_random_numbers(listRandomRange))
    elif(sortType == 'merge_sorte'):
        for i in range(1):
            sort.merge_sort(rand.create_random_numbers(listRandomRange))
    elif(sortType == 'insertion_sort' and listRandomRange <= 100000):
        for i in range(1):
            sort.insertion_sort(rand.create_random_numbers(listRandomRange))
    elif(sortType == 'quick_sort'):
        for i in range(1):
            sort.quickSort(rand.create_random_numbers(
                listRandomRange), 0, listRandomRange - 1)
    elif(sortType == 'counting_sort'):
        for i in range(1):
            sort.counting_sort(rand.create_random_numbers(
                listRandomRange), listRandomRange)
    fim = time.time()
    return (fim - inicio)


def main():
    algorithms = ['bubble_sort', 'merge_sorte',
                    'insertion_sort', 'quick_sort', 'counting_sort']
    list_media = []
    values = [1000, 10000, 100000, 1000000, 10000000]
    #values = [1000, 10000]
    df = pd.DataFrame(columns=['Algoritimos', 'N = 1000', 'N = 10000', 'N = 100000', 'N = 1000000', 'N = 10000000'])
    for i in range(len(algorithms)):
        time_list = []
        for j in range(len(values)):
            time_list.append(handlerTime(algorithms[i], values[j]))
            media = 0
            for time in time_list:
               media = media + time
               media = media/10

               print('media ', algorithms[i], media, values[j])
               list_media.append(media)
            print(list_media)

            df.loc[i] = [algorithms[i]] + list_media
            list_media = []

    df.to_excel('./resultado.xlsx')

main()



