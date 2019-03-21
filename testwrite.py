def writeCsv(self, fileName):
    with open(fileName, "w", newline='') as fileOutput:
        writer = csv.writer(fileOutput)
        for rowNumber in range(self.model.rowCount()):
            fields = [
                self.model.data(
                    self.model.index(rowNumber, columnNumber),
                    QtCore.Qt.DisplayRole
                )
                for columnNumber in range(self.model.columnCount())
            ]
            print(fields)
            writer.writerow(fields)