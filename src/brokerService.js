import axios from 'axios';

export const brokerService = {
    signup,
    getBrokers
};

const SIGNUP_URL = '/api/sign-up';
const GET_BROKERS_URL = '/api/brokers';

function signup(first_name, last_name, email, address) {
    return axios.post(SIGNUP_URL, {
        first_name: first_name,
        last_name: last_name,
        email: email,
        address: address
    }).then(response => {
        return response.data
    }).catch(response => {
        return response.response.data
    })
}

function getBrokers() {
    return axios.get(GET_BROKERS_URL)
    .then(response => {
        return response.data
    }).catch(response => {
        return response.response.data
    })
}