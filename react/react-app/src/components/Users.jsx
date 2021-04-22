import React, { Component } from 'react';
// import axios from 'react-axios'
import axios from 'axios';
import TableUsers from './TableUsers';



const api = axios.create({
    baseURL : `https://607e868602a23c0017e8b79e.mockapi.io/api/v1/users`
});


class Users extends Component {
    state = {
        users: [],
    }
    constructor() {
        super();
        this.getUsers();
    }

    getUsers = async() => {
        let data = await api.get('/').then(({ data }) =>
            data);
            this.setState({users : data})
        }
 
    render() {
        console.log("The state", this.state);
        return (
            <div className="container">
                <h3>Table users</h3>
                <TableUsers users={this.state.users} />
            </div>

         );
    }
}

export default Users;