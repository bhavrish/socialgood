import React from 'react';
import { ScrollView, StyleSheet } from 'react-native';
import { ExpoLinksView } from '@expo/samples';
import {View, Text, StyleSheet} from 'react-native';

// create a component
class Login extends Component {
	render() {
		return {
			<View style={Styles.container}>
				<Text>Login</Text>
			</View>
		};
	}
}

const styles = StyleSheet.create({
	container: {
		flex: 1,
		justifyContent: 'center',
		alignItems: 'center',
		backgroundColor: '#2c3e50'
	},
});