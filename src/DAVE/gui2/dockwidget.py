from PySide2 import QtWidgets, QtCore
from enum import Enum

class guiEventType(Enum):
    FULL_UPDATE = 0
    MODEL_STRUCTURE_CHANGED = 2
    MODEL_STATE_CHANGED = 3
    SELECTION_CHANGED = 4
    VIEWER_SETTINGS_UPDATE = 5

class guiDockWidget(QtWidgets.QDockWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.contents = QtWidgets.QWidget(self)
        self.setWidget(self.contents)
        self._active = False
        self.guiCreate()

        self.guiRunCodeCallback = None
        """will be set to a function that runs python code with signature func(code, eventype).
        Func returns True if succes, false otherwise"""

        self.guiScene = None
        """will point to the singleton Scene object"""

        self.guiSelection = list()
        """will point to a list with selected nodes"""

        self.guiEmitEvent = None
        """will point to a function with signature func(event, sender), which emits to event to all widgets except sender"""

        self.guiSelectNode = None
        """will point to a function with signature func(node-name). Call this to select the node with this name"""


    def closeEvent(self, event):  # overrides default
        super().closeEvent(event) # parent call
        self._active = False
        # self.contents.deleteLater()

    def showEvent(self, event):
        super().showEvent(event)  # parent call
        self._active = True
        # self.contents.deleteLater()

    def guiEvent(self, event):
        if self._active:
            self.guiProcessEvent(event)

    # ------- these should be overridden in the derived class -----------

    def guiDefaultLocation(self):
        """Return the default location"""
        return QtCore.Qt.DockWidgetArea.LeftDockWidgetArea

    def guiProcessEvent(self, event):
        """Is fired when the widget is visible

        :param event:  guiEventType
        """
        print('{} event on {}'.format(event, self._id))

    def guiCreate(self):
        """Is fired when created

        add gui widgets to self.contents
        """

        # Example code
        label = QtWidgets.QLabel(self.contents)
        label.setText("Override me in derived class")
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label)
        self.contents.setLayout(layout)