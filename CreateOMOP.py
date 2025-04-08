import random
from datetime import datetime
import os

class Main:
    def __init__(self):
        self.ob_concept = []

    @staticmethod
    def do_data():

        number_of_patients: int = 10
        obs_per_patient: int = 5;
        meas_per_patient: int = 5;
        clin_per_patient: int = 5;


        # Initialize the values from the original Java code
        obs_values = "46272985,4030271,4097489,4084364,4083951,37152689"
        ob_concepts = obs_values.split(",")

        clin_values = "37169474"
        clin_concepts = clin_values.split(",")

        meas_values = "19569568,3033825,35984039,3037597,3019850,19556060,35947319,19635780,1809364,3965996,35947257,19642719,3024516,19541410,19540727,42528818,3023734,21491552,35948575,35960033,3015466,19533021"
        meas_concepts = meas_values.split(",")

        # should stay fixed
        obs_types_values = "32833,32859,32839,32814,32857,32818,32850,32827,32864,32881,32875,32874,32882,32866,705183,32873,32852,32868,32809,32829,32832,32862,32856,32816,32886,32838,32842,32879,32834,32878,32843,32863,32885,32884,32836,32877,32871,32870,32847,32861,32858,32835,32826,32812,32854,32845,32830,32819,32822,32865"
        ob_types = obs_types_values.split(",")

        gender_values = "8532,8507"
        genders = gender_values.split(",")

        race_values = "38003575,38003580,38003613,38003606,8515,38003579,38003597,38003584,38003577,38003591,38003611,38003593,38003615,38003592,38003616,38003587,38003574,38003583,38003604,38003605,38003585,38003576,38003596,38003610,38003607,8527,38003612,38003614,38003586,38003609,38003603,38003572,38003598,8657,38003573,38003594,8516,38003600,38003599,38003590,38003595,38003588,38003581,38003608,38003578,8557,38003602,38003582,38003589,38003601"
        race = race_values.split(",")

        ethnicity_values = "38003563,38003564"
        ethnicity = ethnicity_values.split(",")

        person = []
        obs = []
        clins = []
        meas = []

        count_total:int = 0
        ob_id:int = 1
        clin_id:int = 1
        meas_id:int = 1

        # Open all files at once using with statement
        with open("observation.csv", "w") as obs_writer, \
             open("person.csv", "w") as person_writer, \
             open("clinical.csv", "w") as clin_writer, \
             open("measurement.csv", "w") as meas_writer:

            for pat_id in range(1, number_of_patients):
                # Generate person data
                gender_select = random.randint(0, len(genders) - 1)
                ethnicity_select = random.randint(0, len(ethnicity) - 1)
                race_select = random.randint(0, len(race) - 1)

                year_to_use = random.randint(1920, 2020)
                month_to_use = random.randint(1, 12)
                day_to_use = random.randint(1, 28)

                person.append(f"{pat_id},{genders[gender_select]},{year_to_use},{month_to_use},{day_to_use},{year_to_use}-{month_to_use}-{day_to_use},{race[race_select]},{ethnicity[ethnicity_select]},,,,,,,,,,")

                # Generate observation data
                for _ in range(obs_per_patient):
                    ob_select = random.randint(0, len(ob_concepts) - 1)
                    ob_type_select = random.randint(0, len(ob_types) - 1)

                    ob_year = random.randint(year_to_use, 2023)
                    ob_month = random.randint(1, 12)
                    ob_day = random.randint(1, 28)

                    month = f"0{ob_month}" if ob_month < 10 else str(ob_month)
                    day = f"0{ob_day}" if ob_day < 10 else str(ob_day)

                    obs.append(f"{ob_id},{pat_id},{ob_concepts[ob_select]},{ob_year}-{month}-{day},,{ob_types[ob_type_select]},,,,,,,,,,,,,,,")
                    ob_id += 1

                # Generate measurement data
                for _ in range(meas_per_patient):
                    meas_select = random.randint(0, len(meas_concepts) - 1)
                    ob_type_select = random.randint(0, len(ob_types) - 1)
                    meas_value = random.randint(0, 100)

                    ob_year = random.randint(year_to_use, 2023)
                    ob_month = random.randint(1, 12)
                    ob_day = random.randint(1, 28)

                    month = f"0{ob_month}" if ob_month < 10 else str(ob_month)
                    day = f"0{ob_day}" if ob_day < 10 else str(ob_day)

                    meas.append(f"{meas_id},{pat_id},{meas_concepts[meas_select]},{ob_year}-{month}-{day},,,{ob_types[ob_type_select]},,{meas_value},,,,,,,,,,,,,,")
                    meas_id += 1

                # Generate clinical data
                for _ in range(clin_per_patient):
                    clin_select = random.randint(0, len(clin_concepts) - 1)
                    clin_type_select = random.randint(0, len(ob_types) - 1)

                    ob_year = random.randint(year_to_use, 2023)
                    ob_month = random.randint(1, 12)
                    ob_day = random.randint(1, 28)

                    month = f"0{ob_month}" if ob_month < 10 else str(ob_month)
                    day = f"0{ob_day}" if ob_day < 10 else str(ob_day)

                    clins.append(f"{clin_id},{pat_id},{clin_concepts[clin_select]},{ob_year}-{month}-{day},,{ob_year}-{month}-{day},,{ob_types[clin_type_select]},,,,,,,,")
                    clin_id += 1

                if count_total == 50000:
                    for s in obs:
                        obs_writer.write(s + "\n")
                    for s in clins:
                        clin_writer.write(s + "\n")
                    for s in meas:
                        meas_writer.write(s + "\n")
                    count_total = 0
                    obs.clear()
                    clins.clear()
                    meas.clear()

                count_total += 1

            # Write remaining data
            for s in person:
                person_writer.write(s + "\n")
            for s in clins:
                clin_writer.write(s + "\n")
            for s in obs:
                obs_writer.write(s + "\n")
            for s in meas:
                meas_writer.write(s + "\n")

    @staticmethod
    def main():
        try:
            Main.do_data()
        except IOError as e:
            print(e)
            print("FAILED")
        print("here")

if __name__ == "__main__":
    Main.main()
