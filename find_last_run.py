def find_last_run():
    import os

    directories = os.listdir('runs/track/weights/')
    run_numbers = []

    for i in directories:
        run_numbers.append(i[30:])

    try:
        run_numbers[run_numbers.index('17')] = '170'
    except ValueError:
        pass

    for i in range(len(run_numbers)):
        run_numbers[i] = run_numbers[i][2:]
        run_numbers[i] = int(run_numbers[i])

    run_numbers.sort()

    last_run_number = run_numbers[-1]

    if last_run_number == 0:
        last_run_number = ''
    last_run_number = str(last_run_number)

    answer = f'best_final_osnet_ibn_x1_0_MSMT17{last_run_number}'

    return answer
