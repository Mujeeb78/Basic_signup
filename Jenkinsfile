pipeline {
	agent any
	stages {

		stage('Python Build') {
			steps {
				sh 'git checkout development_sheethal'
				sh 'ls -lart'
				sh 'python3 manage.py migrate'
				sh 'python3 manage.py runserver 0.0.0.0:8000'
			}

		}

		stage('stop server') {
			steps {
				sh 'sudo killall -9 python3'
			}

		}
	}
}
