# QML Snippets for [Visual Studio Code](https://code.visualstudio.com/)

This extension for Visual Studio Code adds snippets for the [QML](http://www.qt.io/) language (Qt Meta-object Language).

The extension is based on the Sublime QML extension by Sergey Kozlov: https://github.com/ThomasVogelpohl/vsc-qml-snippets

![Use Extension](images/animationSnippets.gif)

## Prerequisites:
The qml file extension needs to be registered as a known file type with VSCode.
The easiest way is to use the QML language syntax extension from Baptist BENOIST: https://github.com/bbenoist/vscode-qml

## Usage
Type part of a snippet, press `enter`, and the snippet unfolds.

### QML Snippets
| Trigger                | Content |
| :-------               | :------- |
|alias                   |	property alias name :val|
|anchors                 |	anchors. :parent.
|anchors (all sides)     |	anchors.left: parent.left<br />anchors.top: parent.top<br />anchors.right: parent.right<br />anchors.bottom: parent.bottom
|anchors.centerIn        |	anchors.centerIn: parent
|anchors.fill            |	anchors.fill: parent
|anchors.horizontalCenter|	anchors.horizontalCenter: parent.horizontalCenter
|anchors.margins         |	anchors.margins: 0
|anchors.verticalCenter  |	anchors.verticalCenter: parent.verticalCenter
|color                   |	color: \"#\"
|component.onCompleted:  |	Component.onCompleted:
|connections             |	Connections {\n    target: \n    on \n
|console.log             |	console.log(" :")
|console.log + var       |	console.log(" :" + var)
|function                |	function name(argument) {<br />&nbsp;    // body...<br />}
|layout                  |	Layout.fillWidth: true\nLayout.fillHeight: :true
|layout.fillHeight       |	Layout.fillHeight: true
|layout.fillWidth        |	Layout.fillWidth: true
|mouse                   |	MouseArea {<br />&nbsp;    anchors.fill: parent<br />&nbsp;    cursorShape: Qt.PointingHandCursor<br />&nbsp;    hoverEnabled: false<br />&nbsp;    onEntered: {<br />&nbsp;    onExited: {<br />&nbsp;    onWheel: {<br />&nbsp;    onClicked: <br />}
|property                |	property var name
|default property        |	default property var name
|readonly property       |	readonly property var name:
|QtObject                |	QtObject {<br />&nbsp;    id:<br />}
|Rectangle               |	Rectangle {<br />&nbsp;    width: 10<br />&nbsp;    height: 10<br />&nbsp;    color: transparent<br />}
|signal                  |	signal name()
|stack.onStatusChanged   |	Stack.onStatusChanged: {<br />&nbsp;    if (Stack.status == Stack.Active)<br />&nbsp;&nbsp;        ;<br />&nbsp;    else if (Stack.status == Stack.Inactive)<br />&nbsp;&nbsp; ;<br />}
