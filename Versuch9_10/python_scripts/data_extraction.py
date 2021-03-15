"""Small script to extract the LTSpice Data (logs) for usage with Origin Pro"""

def main(case: int = 0):
    """Main method

    @param case: case = 1 => add steps for core (x) in output
    """

    # Input files
    inp_files = ["Reihenschwing", "Parallelschwing"]

    for file in inp_files:
        input_file = open(file+".log","r")
        lines = input_file.readlines()

        # Needed variables for extraction
        transformed = []
        data = []
        index = -1
        meas = False

        # First two hits have to be excluded
        curr_step = -1

        # Total number of lines with data
        max_steps = 65

        if (case == 1):
            data.append([])
            for i in range(1,max_steps+1):
                step_x = (i-1)/2
                step_x = str(step_x).replace(".",",")
                data[0].append(step_x)

                index += 1

        for line in lines:
            # Indicator where the extraction should start
            if line.__contains__("Measurement"):
                meas = True
                data.append([])
                index += 1
                curr_step = -1
            elif (curr_step == max_steps+1):
                meas = False

            if (meas):
                if curr_step > 0:
                    # Extract the .meas data
                    # Attention: Origin uses the format 1.000,00 for imports
                    # (or my settings are incorrect)
                    dat = line.split('\t')[1].replace(".",",")

                    data[index].append(dat)

                curr_step += 1

        # Reformat data list
        # data = [[1, 2, 3, 4, ...], [a, b, c, d, ...]]
        # output = [[1, a], [2, b], [3, c], ...]
        output = []
        for jj in range(len(data[0])):
            rearrange = ""
            for ii in range(len(data)):
                # Tab seperated
                rearrange += data[ii][jj] + "\t"
            output.append(rearrange[:-1]+"\n")
        print(output)

        # Write data to file        
        with open(file+"_extracted.dat", "w+") as output_file:
            output_file.writelines(output)
        


if __name__ == "__main__":
    main()
